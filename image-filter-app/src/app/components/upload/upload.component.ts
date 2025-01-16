import {Component} from '@angular/core';
import {MatButton} from "@angular/material/button";
import {ApiService} from "../../services/api.service";

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [
    MatButton
  ],
  templateUrl: './upload.component.html',
  styleUrl: './upload.component.scss'
})
export class UploadComponent {
  selectedFile: File | null = null;

  constructor(private apiService: ApiService) {
  }

  onFileSelected(event: Event): void {
    const target = event.target as HTMLInputElement;
    if (target.files) {
      this.selectedFile = target.files[0];
    }
  }

  uploadImage(): void {
    if (this.selectedFile) {
      this.apiService.uploadImage(this.selectedFile).subscribe((response) => {
        console.log('Image uploaded successfully:', response);
      });
    }
  }
}
