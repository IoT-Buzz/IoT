package com.example.dragospc.nodemcu1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class LED_activity extends AppCompatActivity {

    private static ImageView light1,tubeLight,nightLight,fan;
    public static String commd;
    private int statusl1 = 0,statustl=0,statusnl=0,statusf=0;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_led_activity);

        light1 =(ImageView) findViewById(R.id.l1);
        tubeLight = (ImageView)findViewById(R.id.tl1);
        nightLight = (ImageView)findViewById(R.id.nl1);
        fan = (ImageView)findViewById(R.id.f1);

        light1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


               if(statusl1==0)
               {
                   commd = "led1on";
                   on1 process1 = new on1();
                   process1.execute();
                   statusl1 =1;
                   light1.setImageResource(R.drawable.light1_on);
               }

               else
               {
                   commd="led1off";
                   on1 process1 = new on1();
                   process1.execute();
                   statusl1=0;
                   light1.setImageResource(R.drawable.light1_off);
               }
            }
        });

        tubeLight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                if(statustl==0)
                {
                    commd = "tubeLighton";
                    on1 process1 = new on1();
                    process1.execute();
                    statustl =1;
                    tubeLight.setImageResource(R.drawable.tubelight_on);
                }

                else
                {
                    commd="tubeLightoff";
                    on1 process1 = new on1();
                    process1.execute();
                    statustl=0;
                    tubeLight.setImageResource(R.drawable.tubelight_off);
                }
            }
        });

        nightLight.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                if(statusnl==0)
                {
                    commd = "nightLighton";
                    on1 process1 = new on1();
                    process1.execute();
                    statusnl =1;
                    nightLight.setImageResource(R.drawable.nightlamp_on);
                }

                else
                {
                    commd="nightLightoff";
                    on1 process1 = new on1();
                    process1.execute();
                    statusnl=0;
                    nightLight.setImageResource(R.drawable.nightlamp_off);
                }
            }
        });


        fan.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                if(statusf==0)
                {
                    commd = "fanon";
                    on1 process1 = new on1();
                    process1.execute();
                    statusf =1;
                    fan.setImageResource(R.drawable.fan_on);
                }

                else
                {
                    commd="fanoff";
                    on1 process1 = new on1();
                    process1.execute();
                    statusf=0;
                    fan.setImageResource(R.drawable.fan_off);
                }
            }
        });
    }
}
