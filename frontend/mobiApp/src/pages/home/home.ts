import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { SignupPage } from '../signup/signup';
import { UseraccountPage } from '../useraccount/useraccount';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {

  uName:string;
  password:string;
  dis:string;
  users :FirebaseListObservable<any>;

  constructor(public navCtrl: NavController,public afd:AngularFireDatabase) {

  }

  signup(){

    this.navCtrl.push(SignupPage);

  }

  login(){

    var pwd;


    try{


          this.users = this.afd.list('/profile/'+ this.uName).valueChanges();
          this.users.forEach(element => {
          pwd=element[0]["password"];
          

            if(pwd==this.password){
              this.navCtrl.push(UseraccountPage,{data:this.uName});
            }
            else{
              this.dis = "Incorrect User Name or Password";
            }
          });


}
catch(e){
  console.log("ERROR");
}









    // this.navCtrl.push(UseraccountPage,{data:this.uName});
    // console.log(this.uName);

  }

}
