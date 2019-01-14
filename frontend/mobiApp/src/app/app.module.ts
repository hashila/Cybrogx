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

import { AngularFireModule } from '@angular/fire';
import { AngularFirestoreModule } from '@angular/fire/firestore';
import { AngularFireStorageModule } from '@angular/fire/storage';
import { AngularFireAuthModule } from '@angular/fire/auth';


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
    AngularFirestoreModule, // imports firebase/firestore, only needed for database features
    AngularFireAuthModule, // imports firebase/auth, only needed for auth features,
    AngularFireStorageModule // imports firebase/storage only needed for storage features

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
