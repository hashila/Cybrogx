import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';


/**
 * Generated class for the HomewindowPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-homewindow',
  templateUrl: 'homewindow.html',
})
export class HomewindowPage {

  users :FirebaseListObservable<any>;

  constructor(public navCtrl: NavController, public navParams: NavParams,afd :AngularFireDatabase) {
    var uName :string;
    var fullname :string;
    uName = this.navParams.get('data');
    console.log(uName);
    this.users = afd.list('/news/'+ uName).valueChanges();


  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad HomewindowPage');
  }

}
