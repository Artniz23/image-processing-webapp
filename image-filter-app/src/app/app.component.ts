import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from '@angular/router';
import {UploadComponent} from "./components/upload/upload.component";
import {FilterSelectorComponent} from "./components/filter-selector/filter-selector.component";
import {ImageViewerComponent} from "./components/image-viewer/image-viewer.component";
import {ApiService} from "./services/api.service";
import {MatButton} from "@angular/material/button";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, UploadComponent, FilterSelectorComponent, ImageViewerComponent, MatButton],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  originalImage: string | null = null;
  filteredImage: string | null = null;
  uploadedFile: File | null = null;
  filteredFile: File | null = null;
  selectedFilter: string | null = null;

  constructor(private apiService: ApiService) {
  }

  onFileUploaded(file: File): void {
    this.uploadedFile = file;
    const reader = new FileReader();
    reader.onload = () => {
      this.originalImage = reader.result as string;
    };
    reader.readAsDataURL(file);
  }

  onDeletedFile(): void {
    this.originalImage = null;
    this.filteredImage = null;
    this.uploadedFile = null;
    this.filteredFile = null;
    this.selectedFilter = null;
  }

  onFilterSelected(filter: string): void {
    this.selectedFilter = filter;

    if (this.uploadedFile) {
      this.apiService.applyFilter(filter, this.uploadedFile).subscribe((blob) => {
        const objectURL = URL.createObjectURL(blob);
        this.filteredImage = objectURL;
        this.filteredFile = new File([blob], "filteredImage", { type: this.uploadedFile!.type });
      });
    }
  }

  saveImage(): void {
    this.apiService.saveImage(this.selectedFilter!, this.uploadedFile!, this.filteredFile!).subscribe((data) => {
      console.log('data', data);
    });
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
}
