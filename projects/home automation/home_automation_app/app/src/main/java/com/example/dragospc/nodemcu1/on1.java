package com.example.dragospc.nodemcu1;

import android.os.AsyncTask;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;

import static com.example.dragospc.nodemcu1.LED_activity.commd;
import static com.example.dragospc.nodemcu1.MainActivity.texr;

public class on1 extends AsyncTask<Void,Void,String> {
    @Override
    protected String doInBackground(Void... voids) {
        try {
            URL url = new URL("http://"+texr+"/"+commd);
            HttpURLConnection httpURLConnection = (HttpURLConnection) url.openConnection();
            InputStream inputStream = httpURLConnection.getInputStream();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));


        }
        catch (MalformedURLException e)
        {

        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return null;
    }
    @Override
    protected void onPostExecute(String aVoid) {
        super.onPostExecute(aVoid);

    }
}
