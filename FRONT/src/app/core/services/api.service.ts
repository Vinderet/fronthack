import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';


@Injectable({
  providedIn: 'root', // Сервис доступен на уровне всего приложения
})
export class ApiService {
  private baseUrl = environment.apiUrl; // Базовый URL API

  constructor(private http: HttpClient) {}

  /**
   * Выполняет GET-запрос к API.
   * @param endpoint - Конечная точка API (например, 'users').
   * @param params - Параметры запроса (опционально).
   * @returns Observable с ответом от сервера.
   */
  get<T>(endpoint: string, params?: HttpParams): Observable<T> {
    const url = `${this.baseUrl}/${endpoint}`;
    return this.http.get<T>(url, { params });
  }

  /**
   * Выполняет POST-запрос к API.
   * @param endpoint - Конечная точка API (например, 'users').
   * @param body - Тело запроса.
   * @param headers - Заголовки запроса (опционально).
   * @returns Observable с ответом от сервера.
   */
  post<T>(endpoint: string, body: any, headers?: HttpHeaders): Observable<T> {
    const url = `${this.baseUrl}/${endpoint}`;
    return this.http.post<T>(url, body, { headers });
  }

  /**
   * Выполняет PUT-запрос к API.
   * @param endpoint - Конечная точка API (например, 'users/1').
   * @param body - Тело запроса.
   * @param headers - Заголовки запроса (опционально).
   * @returns Observable с ответом от сервера.
   */
  put<T>(endpoint: string, body: any, headers?: HttpHeaders): Observable<T> {
    const url = `${this.baseUrl}/${endpoint}`;
    return this.http.put<T>(url, body, { headers });
  }

  /**
   * Выполняет DELETE-запрос к API.
   * @param endpoint - Конечная точка API (например, 'users/1').
   * @returns Observable с ответом от сервера.
   */
  delete<T>(endpoint: string): Observable<T> {
    const url = `${this.baseUrl}/${endpoint}`;
    return this.http.delete<T>(url);
  }

  /**
   * Выполняет PATCH-запрос к API.
   * @param endpoint - Конечная точка API (например, 'users/1').
   * @param body - Тело запроса.
   * @param headers - Заголовки запроса (опционально).
   * @returns Observable с ответом от сервера.
   */
  patch<T>(endpoint: string, body: any, headers?: HttpHeaders): Observable<T> {
    const url = `${this.baseUrl}/${endpoint}`;
    return this.http.patch<T>(url, body, { headers });
  }
}