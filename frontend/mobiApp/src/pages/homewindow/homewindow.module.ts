import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { HomewindowPage } from './homewindow';

@NgModule({
  declarations: [
    HomewindowPage,
  ],
  imports: [
    IonicPageModule.forChild(HomewindowPage),
  ],
})
export class HomewindowPageModule {}
