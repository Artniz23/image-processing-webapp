import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {
  }

  applyFilter(filterName: string, file: Blob): Observable<Blob> {
    const formData = new FormData();
    formData.append('filter_name', filterName);
    formData.append('file', file);
    return this.http.post(`${this.apiUrl}/process`, formData, {responseType: 'blob'});
  }

  saveImage(filterName: string, original_image: Blob, processedImage: Blob): Observable<any> {
    const formData = new FormData();
    formData.append('filter_name', filterName);
    formData.append('original_image_file', original_image);
    formData.append('processed_image_file', processedImage);

    return this.http.post(`${this.apiUrl}/save`, formData);
  }
}
