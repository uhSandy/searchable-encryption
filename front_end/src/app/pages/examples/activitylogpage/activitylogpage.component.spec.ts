import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActivitylogpageComponent } from './activitylogpage.component';

describe('ActivitylogpageComponent', () => {
  let component: ActivitylogpageComponent;
  let fixture: ComponentFixture<ActivitylogpageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ActivitylogpageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ActivitylogpageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
