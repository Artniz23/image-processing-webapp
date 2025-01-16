import {Component} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterOutlet} from '@angular/router';
import {UploadComponent} from "./components/upload/upload.component";
import {FilterSelectorComponent} from "./components/filter-selector/filter-selector.component";
import {ImageViewerComponent} from "./components/image-viewer/image-viewer.component";
import {ApiService} from "./services/api.service";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, UploadComponent, FilterSelectorComponent, ImageViewerComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  originalImage: string | null = null;
  filteredImage: string | null = null;
  uploadedFile: File | null = null;

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

  onFilterSelected(filter: string): void {
    if (this.uploadedFile) {
      this.apiService.applyFilter(filter, this.uploadedFile).subscribe((blob) => {
        const objectURL = URL.createObjectURL(blob);
        this.filteredImage = objectURL;
      });
    }
  }
}
