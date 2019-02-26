import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { HomewindowPage } from '../homewindow/homewindow';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';



@IonicPage()
@Component({
  selector: 'page-useraccount',
  templateUrl: 'useraccount.html',
})
export class UseraccountPage {

   users :FirebaseListObservable<any>;
   name:string;


  constructor(public navCtrl: NavController, public navParams: NavParams,afd :AngularFireDatabase) {
    var uName :string;
    var fullname :string;

    uName = this.navParams.get('data');


    this.name = uName;
    // console.log(this.name);
    this.users = afd.list('/profile/'+ uName).valueChanges();

    this.users.forEach(element => {
            console.log(element[0]["address"]);
        });

  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad UseraccountPage');
  }
  showHome(){
    this.navCtrl.push(HomewindowPage,{data:this.name});
  }



}
