import {Component, Input} from '@angular/core';
import {CommonModule, NgOptimizedImage} from "@angular/common";

@Component({
  selector: 'app-image-viewer',
  standalone: true,
  imports: [CommonModule, NgOptimizedImage],
  templateUrl: './image-viewer.component.html',
  styleUrl: './image-viewer.component.scss'
})
export class ImageViewerComponent {
  @Input() originalImage: string | null = null;
  @Input() filteredImage: string | null = null;
}
