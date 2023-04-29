import 'package:ems/reusbale_widgets_constants.dart';
import 'package:flutter/material.dart';
import 'package:ems/landing_page_afterlogin.dart';
// import 'package:ems/PopularNow.dart';

// import 'package:ems/landing_page_afterlogin.dart';
void main() {
  runApp(
    MaterialApp(
      theme: ThemeData(
        primarySwatch: kThemeColor,
        appBarTheme: AppBarTheme(
          iconTheme: IconThemeData(color: Colors.white),
          color: kThemeColor, //<-- SEE HERE
        ),
      ),
      // home: MyApp(),
      //  home: MyHomePage(),
      home: HomePage(),
      // home: PopularNow(),
    ),
  );
}
