import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { AngularFirestore } from '@angular/fire/firestore';
import { Observable } from 'rxjs';




@IonicPage()
@Component({
  selector: 'page-signup',
  templateUrl: 'signup.html',
})
export class SignupPage {

  items: Observable<any[]>;


  constructor(public navCtrl: NavController, public navParams: NavParams,db: AngularFirestore) {

    this.items = db.collection('items').valueChanges();


  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad SignupPage');
  }

}
