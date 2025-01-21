import {Component, inject, signal} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from '@angular/router';
import {UploadComponent} from "./components/upload/upload.component";
import {FilterSelectorComponent} from "./components/filter-selector/filter-selector.component";
import {ImageViewerComponent} from "./components/image-viewer/image-viewer.component";
import {ApiService} from "./services/api.service";
import {MatButton} from "@angular/material/button";
import {MatProgressSpinner} from "@angular/material/progress-spinner";
import {finalize, Observable, tap} from "rxjs";
import {MatSnackBar} from "@angular/material/snack-bar";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, UploadComponent, FilterSelectorComponent, ImageViewerComponent, MatButton, MatProgressSpinner],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  originalImage: string | null = null;
  filteredImage: string | null = null;
  uploadedFile: File | null = null;
  filteredFile: File | null = null;
  selectedFilter: string | null = null;
  availableFilters: any[] = [];

  private snackBar = inject(MatSnackBar);

  isLoading = signal(false);

  constructor(private apiService: ApiService) {
  }

  onFileUploaded(file: File): void {
    this.isLoading.set(true);

    this.uploadedFile = file;
    const reader = new FileReader();
    reader.onload = () => {
      this.originalImage = reader.result as string;
    };
    reader.readAsDataURL(file);

    this.requestFilters()
      .pipe(
        tap((filters) => {
          this.availableFilters = filters;
        }),
        finalize(() => this.isLoading.set(false))
      )
      .subscribe();
  }

  onDeletedFile(): void {
    this.originalImage = null;
    this.filteredImage = null;
    this.uploadedFile = null;
    this.filteredFile = null;
    this.selectedFilter = null;
  }

  onFilterSelected(filter: string): void {
    this.isLoading.set(true);

    this.selectedFilter = filter;

    if (this.uploadedFile) {
      this.apiService.applyFilter(filter, this.uploadedFile)
        .pipe(
          tap((blob) => {
            const objectURL = URL.createObjectURL(blob);
            this.filteredImage = objectURL;
            this.filteredFile = new File([blob], "filteredImage", {type: this.uploadedFile!.type});
          }),
          finalize(() => this.isLoading.set(false))
        )
        .subscribe();
    }
  }

  saveImage(): void {
    this.isLoading.set(true);

    this.apiService.saveImage(this.selectedFilter!, this.uploadedFile!, this.filteredFile!)
      .pipe(
        tap((imageData: any) => {
          this.snackBar.open(`Изображение с id - ${imageData.id} сохранено успешно`, 'Ок');
        }),
        finalize(() => this.isLoading.set(false))
      )
      .subscribe();
  }

  downloadImage(): void {
    const url = URL.createObjectURL(this.filteredFile!);

    const link = document.createElement("a");
    link.href = url;
    link.download = this.filteredFile!.name;

    document.body.appendChild(link);
    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  }

  private requestFilters(): Observable<any[]> {
    return this.apiService.getFilters();
  }
}
