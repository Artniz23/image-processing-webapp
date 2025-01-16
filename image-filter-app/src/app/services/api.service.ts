import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {
  }

  uploadImage(file: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post(`${this.apiUrl}/upload`, formData);
  }

  applyFilter(filterName: string, file: File): Observable<Blob> {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('filter', filterName);
    return this.http.post(`${this.apiUrl}/apply_filter`, formData, {responseType: 'blob'});
  }
}
