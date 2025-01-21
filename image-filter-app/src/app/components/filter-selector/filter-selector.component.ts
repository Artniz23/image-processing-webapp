import {Component, EventEmitter, Output} from '@angular/core';
import {MatFormField, MatLabel} from "@angular/material/form-field";
import {MatOption, MatSelect} from "@angular/material/select";
import {MatButton} from "@angular/material/button";
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-filter-selector',
  standalone: true,
  imports: [
    CommonModule,
    MatFormField,
    MatSelect,
    MatOption,
    MatButton,
    MatLabel
  ],
  templateUrl: './filter-selector.component.html',
  styleUrl: './filter-selector.component.scss'
})
export class FilterSelectorComponent {
  filters = ['grayscale', 'sepia', 'blur'];
  selectedFilter: string | null = null;

  @Output() filterSelected = new EventEmitter<string>();

  applyFilter(): void {
    if (this.selectedFilter) {
      this.filterSelected.emit(this.selectedFilter);
    }
  }
}
