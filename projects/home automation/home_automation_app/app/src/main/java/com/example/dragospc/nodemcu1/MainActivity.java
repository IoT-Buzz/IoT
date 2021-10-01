package com.example.dragospc.nodemcu1;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
    private EditText ipxx1;
    private static ImageView room1;
    public static String texr;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        room1 = (ImageView) findViewById(R.id.r1);
        ipxx1=(EditText) findViewById(R.id.ipadd);

        room1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                texr=ipxx1.getText().toString();
                Intent ht1 = new Intent(MainActivity.this,LED_activity.class);
                startActivity(ht1);
            }
        });
    }
}
