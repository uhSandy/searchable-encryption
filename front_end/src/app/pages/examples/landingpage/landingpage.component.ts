import { Component, OnInit, OnDestroy, Input } from "@angular/core";
import Chart from "chart.js";
import { SearchService } from "src/app/services/search.service";
import { Search } from "../../models/search";
import { HttpClient } from "@angular/common/http";
import { saveAs } from "file-saver";
import { SweetAlert } from "sweetalert/typings/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
const swal: SweetAlert = require('sweetalert');

@Component({
  selector: "app-landingpage",
  templateUrl: "landingpage.component.html"
})
export class LandingpageComponent implements OnInit, OnDestroy {
  isCollapsed = true;
  searchKey = [];
  searchWords: Search;
  @Input()
  searchForm: FormGroup;
  showError = false;
  constructor(public searchService: SearchService, public http: HttpClient, private formBuilder: FormBuilder) {}

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("landing-page");
    this.createForm()
  }

  createForm() {
    this.searchForm = this.formBuilder.group({  
      search: ['', [Validators.required]]
    }); 
  }

  search() {
    if(this.searchForm.valid) {
      console.log(this.searchForm.value.search)
      console.log(this.searchForm.value.search.split(','))
      this.showError = false;
    } else {
      this.showError = true;
    }
    // this.searchWords = {"searchkeys": ["doppler", "intermittent"]}
    this.searchWords = {"searchkeys": this.searchForm.value.search.split(',')};
    this.searchService.searchPost(this.searchWords)
    .subscribe((response: any) => {
      console.log(response)
      this.http.get('assets/files.zip', {responseType: "blob", headers: {'Accept': 'application/zip'}})
        .subscribe(blob => {
          saveAs(blob, 'results.zip');
      });
    },(error: any) => {
      if (error.status == 400) { 
        swal("Oopz!", "Something went wrong!", "error")
        .then(() => {});
      }
    });
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("landing-page");
  }
}
