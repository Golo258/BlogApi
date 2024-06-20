import { Component, EventEmitter, Input, Output} from '@angular/core';
import { NgFor } from '@angular/common';
@Component({
  selector: 'app-submit-tasks',
  standalone: true,
  imports: [NgFor],
  templateUrl: './submit-tasks.component.html',
})
export class SubmitTaskComponent {

    @Output() submitText = new EventEmitter<string>();

}
