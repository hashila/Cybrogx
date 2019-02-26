import { Component,ViewChild  } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { AngularFireDatabase, FirebaseListObservable } from 'angularfire2/database';
import { Chart } from 'chart.js';

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
  ex=0;
  high=0;
  bad=0;

  users :FirebaseListObservable<any>;
  @ViewChild('doughnutCanvas') doughnutCanvas;
  doughnutChart: any;

  constructor(public navCtrl: NavController, public navParams: NavParams,afd :AngularFireDatabase) {
    var uName :string;
    var fullname :string;
    uName = this.navParams.get('data');
    console.log(uName);
    this.users = afd.list('/news/'+ uName).valueChanges();




    this.users.forEach(element => {

      for(var i = 0;i<=element.length-1;i++){
        var x = element[i]["howbad"];
        console.log(x);
        this.ex = this.ex + element[i]["extremecount"];
        this.high = this.high + element[i]["highcount"];
        this.bad = this.bad + element[i]["badcount"];

      }



    });













  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad HomewindowPage');












  }



  show(){


    this.doughnutChart = new Chart(this.doughnutCanvas.nativeElement, {

                type: 'doughnut',
                data: {
                    labels: ["Bad Normal", "Extremely Bad", "Highly Bad"],
                    datasets: [{
                        label: '# of Votes',
                        data: [this.bad, this.ex, this.high],
                        backgroundColor: [
                            'rgba(54, 162, 235, 0.2)',
                            'rgba(255, 99, 132, 0.2)',
                            'rgba(255, 206, 86, 0.2)'

                        ],
                        hoverBackgroundColor: [
                            "#36A2EB",
                            "#FF6384",
                            "#FFCE56"
                        ]
                    }]

                }

            });

            




  }

}
