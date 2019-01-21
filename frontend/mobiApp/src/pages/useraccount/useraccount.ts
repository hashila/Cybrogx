import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomewindowPage } from '../homewindow/homewindow';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

//import { user } from './user';

@IonicPage()
@Component({
  selector: 'page-useraccount',
  templateUrl: 'useraccount.html',
})
export class UseraccountPage {

   users$ :FirebaseListObservable<any>;


  constructor(public navCtrl: NavController, public navParams: NavParams,afd :AngularFireDatabase) {
    var uName :string;
    var fullname :string;
    uName = this.navParams.get('data');
    console.log(uName);
    this.users$ = afd.list('/profile/'+this.uName).valueChanges();

    // this.getProfileInfo();
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UseraccountPage');
  }
  showHome(){
    this.navCtrl.push(HomewindowPage);
  }

  getProfileInfo(){
    this.afd.list('/profile').valueChanges().subscribe(
      data => {
        console.log(JSON.stringify(data));
      }
    );
  }

}
