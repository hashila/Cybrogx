import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { UseraccountPage } from '../useraccount/useraccount';

import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

export interface Item { name: string; }


@IonicPage()
@Component({
  selector: 'page-signup',
  templateUrl: 'signup.html',
})
export class SignupPage {

  uNametxt :string;
  fNametxt :string;
  passwordtxt :string;
  addresstxt :string

  constructor(public navCtrl: NavController, public navParams: NavParams,public db: AngularFireDatabase) {


  }

  ionViewDidLoad() {

    console.log('ionViewDidLoad SignupPage');
  }

  register(){

    this.db.list('/profile/'+this.uNametxt).push({

      username: this.uNametxt,
      fullName: this.fNametxt,
      password: this.passwordtxt,
      address: this.addresstxt

    });
    this.navCtrl.push(UseraccountPage,{data:this.uNametxt});

  }


}
