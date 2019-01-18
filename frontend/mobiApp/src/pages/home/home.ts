import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { SignupPage } from '../signup/signup';
import { UseraccountPage } from '../useraccount/useraccount';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  
  constructor(public navCtrl: NavController) {

  }

  signup(){

    this.navCtrl.push(SignupPage);

  }

  login(name: string){
    this.navCtrl.push(UseraccountPage,{data:name});
    console.log(name);

  }

}
