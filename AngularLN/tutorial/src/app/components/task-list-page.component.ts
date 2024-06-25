import { Component } from '@angular/core';
import { TasksListComponent } from './tasks-list.component';
import { SubmitTaskComponent } from './submit-task.component';
import { Task } from '../types/Tasks';
import { ComponentListState } from '../types/States';
import { NgIf } from '@angular/common';

type ListFetchingError = {
  status: number;
  message: string;
};

@Component({
  selector: 'app-task-list-page',
  standalone: true,
  imports: [TasksListComponent, SubmitTaskComponent, NgIf],
  templateUrl: `./task-list-page.component.html`,
})
export class TaskListPageComponent {
  tasks: Task[] = [];
  listState: ComponentListState = { state: 'idle' };

  private readonly URL = 'http://localhost:3000';

  constructor() {
    this.listState = { state: 'loading' };

    fetch(`${this.URL}/tasks`)
      .then<Task[] | ListFetchingError>((response) => {
        if (response.ok) {
          return response.json();
        } else {
          return { status: response.status, message: response.statusText };
        }
      })
      .then((response) => {
        setTimeout(() => {
          if (Array.isArray(response)) {
            this.listState = {
              state: 'success',
              result: response,
            };
          } else {
            this.listState = {
              state: 'error',
              error: response,
            };
          }
        }, 1200);
      });
  }

  addTask(name: string) {
    // this.tasks.push({
    //   name,
    //   done: false,
    // });
  }
}
