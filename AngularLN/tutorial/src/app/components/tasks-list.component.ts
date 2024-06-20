import { Component, Input} from '@angular/core';
import { NgFor } from '@angular/common';
import { Task } from '../Tasks';
@Component({
  selector: 'app-tasks-list',
  standalone: true,
  imports: [NgFor],
  templateUrl: './tasks-list.component.html',
})
export class TasksListComponent {
  @Input( {required : true}) tasks: Task[] = [];

  toggleDoneStatus(task: Task) {
    task.done = !task.done;
  }
}
