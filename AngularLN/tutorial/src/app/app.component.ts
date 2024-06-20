import { NgFor } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TasksListComponent } from './components/tasks-list.component';
import { SubmitTaskComponent } from './components/submit-task.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TasksListComponent, SubmitTaskComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
  title = 'tutorial';
  tasks = [
    {
      name: 'Simple information',
      done: false,
    },
    {
      name: 'Anothe better information',
      done: true,
    },
  ];

  addTask(name: string) {
    this.tasks.push({
      name: name,
      done: false,
    });
  }
}
