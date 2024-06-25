import { Component, Input } from '@angular/core';
import { TasksListComponent } from './components/tasks-list.component';
import { SubmitTaskComponent } from './components/submit-task.component';
import { Task } from './types/Tasks';
import { TaskListPageComponent } from './components/task-list-page.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TasksListComponent, SubmitTaskComponent, TaskListPageComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})
export class AppComponent {
}
