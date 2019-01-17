import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomewindowPage } from '../homewindow/homewindow';


@IonicPage()
@Component({
  selector: 'page-useraccount',
  templateUrl: 'useraccount.html',
})
export class UseraccountPage {

  uName :String;

  constructor(public navCtrl: NavController, public navParams: NavParams) {
    this.uName = this.navParams.get('uName');

  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UseraccountPage');
  }
  showHome(){
    this.navCtrl.push(HomewindowPage);
  }

}
