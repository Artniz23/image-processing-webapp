import {Component, EventEmitter, Output} from '@angular/core';
import {MatButton} from "@angular/material/button";

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
  isDragOver: boolean = false;
  uploadedFile: File | null = null;

  @Output() uploaded = new EventEmitter<File>;

  @Output() deleted = new EventEmitter<void>();

  // При перетаскивании файла в зону
  onDragOver(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragOver = true;
  }

  // Когда файл покидает зону
  onDragLeave(): void {
    this.isDragOver = false;
  }

  // Когда файл сбрасывают в зону
  onFileDrop(event: DragEvent): void {
    event.preventDefault();
    event.stopPropagation();
    this.isDragOver = false;

    if (event.dataTransfer?.files.length) {
      this.uploadedFile = event.dataTransfer.files[0];
      this.uploaded.emit(this.uploadedFile);
    }
  }

  // Когда файл выбирают через диалог
  onFileSelect(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.uploadedFile = input.files[0];
      this.uploaded.emit(this.uploadedFile);
    }
  }

  // Удалить выбранный файл
  removeFile(): void {
    this.uploadedFile = null;
    this.deleted.emit();
  }
}
