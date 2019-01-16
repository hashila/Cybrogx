import { BrowserModule } from '@angular/platform-browser';
import { ErrorHandler, NgModule } from '@angular/core';
import { IonicApp, IonicErrorHandler, IonicModule } from 'ionic-angular';
import { SplashScreen } from '@ionic-native/splash-screen';
import { StatusBar } from '@ionic-native/status-bar';

import { MyApp } from './app.component';
import { HomePage } from '../pages/home/home';
import { SignupPage } from '../pages/signup/signup';
import { UseraccountPage } from '../pages/useraccount/useraccount';
import { HomewindowPage } from '../pages/homewindow/homewindow';

import { AngularFireModule } from 'angularfire2';
import { AngularFireDatabaseModule } from 'angularfire2/database';



const config = {
    apiKey: "AIzaSyB-0Zcia1IrqEzMn39qp-JrEaGeoON57-Y",
    authDomain: "cybrogx-1543512333299.firebaseapp.com",
    databaseURL: "https://cybrogx-1543512333299.firebaseio.com",
    projectId: "cybrogx-1543512333299",
    storageBucket: "cybrogx-1543512333299.appspot.com",
    messagingSenderId: "1048992728209"
  };

@NgModule({
  declarations: [
    MyApp,
    HomePage,
    SignupPage,
    UseraccountPage,
    HomewindowPage
  ],
  imports: [
    BrowserModule,
    IonicModule.forRoot(MyApp),
    AngularFireModule.initializeApp(config),
    AngularFireDatabaseModule
  ],
  bootstrap: [IonicApp],
  entryComponents: [
    MyApp,
    HomePage,
    SignupPage,
    UseraccountPage,
    HomewindowPage
  ],
  providers: [
    StatusBar,
    SplashScreen,
    {provide: ErrorHandler, useClass: IonicErrorHandler}
  ]
})
export class AppModule {}
