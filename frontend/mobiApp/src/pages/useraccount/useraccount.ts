import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomewindowPage } from '../homewindow/homewindow';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

import { profileList } from '../profileList/profileList';

@IonicPage()
@Component({
  selector: 'page-useraccount',
  templateUrl: 'useraccount.html',
})
export class UseraccountPage {

  person: FirebaseListObservable<profileList[]>;


  constructor(public navCtrl: NavController, public navParams: NavParams,afd :AngularFireDatabase) {
    var uName :string;
    var fullname :string;
    uName = this.navParams.get('data');
    console.log(uName);


    //this.getProfileInfo(uName);
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UseraccountPage');
  }
  showHome(){
    this.navCtrl.push(HomewindowPage);
  }

  getProfileInfo(name :string){
    this.afd.list('/profile').valueChanges().subscribe(
      data => {
        console.log(JSON.stringify(data));
      }
    );
  }

}
