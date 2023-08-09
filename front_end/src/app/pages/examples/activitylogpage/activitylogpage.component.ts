import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-activitylogpage',
  templateUrl: './activitylogpage.component.html',
  styleUrls: ['./activitylogpage.component.scss']
})
export class ActivitylogpageComponent implements OnInit {
  isCollapsed = true;
  constructor() { }

  ngOnInit(): void {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("activity-page");
  }

  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("activity-page");
  }
}
