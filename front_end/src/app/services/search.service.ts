import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Search } from '../pages/models/search';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) { }

  BaseUrl = 'http://localhost:5000';

  searchPost(search: Search): Observable<Search> {
    return this.http.post<Search>(`${this.BaseUrl}/search`, search)
  }
}
