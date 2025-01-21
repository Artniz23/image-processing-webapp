import {Injectable, signal, WritableSignal} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {
  uploadedFile: WritableSignal<File | null> = signal(null);

  constructor() { }
}
