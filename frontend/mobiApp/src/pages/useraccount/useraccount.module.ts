import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { UseraccountPage } from './useraccount';
import { HomewindowPage } from '../homewindow/homewindow';


@NgModule({
  declarations: [
    UseraccountPage,
    HomewindowPage

  ],
  imports: [
    IonicPageModule.forChild(UseraccountPage),
  ],
})
export class UseraccountPageModule {}
