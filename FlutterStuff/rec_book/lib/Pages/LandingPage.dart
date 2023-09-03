import 'package:flutter/material.dart';

class LandingPage extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("RecBook"),
        centerTitle: true,
      ),
      body: Center(
        child: column(
          mainAxisAlignment: MainAxisAlignment.Center,
          childeren: [
            Text('RecBook',
            style: TextStyle(
              color: Colors.black,
              fontSize: 32,
              fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(height: 20,),
            ElevatedButton(
              onPressed: () {
                //Navigator.push(context, MaterialPageRoute(builder: (context) => LoginPage()));
              },
              child: Text('SignUp Face'),
              style: ElevatedButton.styleFrom(
                primary: Colors.blue,
                onPrimary: Colors.white,
              ),
            ),
            SizedBox(height: 20,),
            ElevatedButton(
              onPressed: () {
                //Navigator.push(context, MaterialPageRoute(builder: (context) => LoginPage()));
              },
              child: Text('RollUp Face'),
              style: ElevatedButton.styleFrom(
                primary: Colors.blue,
                onPrimary: Colors.white,
              ),
            ),
          ]
        )
      ),
    );
  }
}