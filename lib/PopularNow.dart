import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:ems/reusbale_widgets_constants.dart';

class PopularNow extends StatefulWidget {
  const PopularNow({super.key});

  @override
  State<PopularNow> createState() => _PopularNowState();
}

class _PopularNowState extends State<PopularNow> {
  TextEditingController eventType = TextEditingController(text: "Marriage");
  TextEditingController city = TextEditingController(text: "Sarajevo");

  void handleSearch() {
    insertrecords();
    // getRecord();
  }
  bool isLoading = true;
  List<dynamic> response = [];

  Future<void> insertrecords() async {
    if (eventType.text != "" || city.text != "") {
      try {
        String uri = "http://127.0.0.1:5000";
        Map<String, dynamic> data = {
          'EventType': eventType.text,
          'City': city.text,
        };
        String jsonData = jsonEncode(data);
        var res = await http.post(
          Uri.parse(uri),
          body: jsonData,
          headers: {"Content-Type": "application/json"},
        );

        var dataJson = jsonDecode(res.body)['data'];
        if (dataJson is String) {
          // Convert the string to a list of dictionaries
          response = List<Map<String, dynamic>>.from(
            jsonDecode(dataJson).map((x) => Map<String, dynamic>.from(x)),
          );
        } else if (dataJson is List) {
          // Use the list directly
          response = dataJson;
        }

        print(response);

        // Check if the response was successful (status code 200)
        if (res.statusCode == 200) {
          print('Success');
          setState(() {
            isLoading = false;
          });
        } else {
          print('Request failed with status code ${res.statusCode}');
        }

      } catch (e) {
        print('Error: $e');
      }
    } else {
      debugPrint("please fill the data");
    }
  }

  @override
  void initState() {
    super.initState();
    insertrecords();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      // Call the onPressed callback of the ButtonText widget
      handleSearch();
      // getRecord();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: kThemeColor,
        title: Text("Popular Now"),
      ),
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(vertical: 20.0),
          child: Column(
            children: [
              // Expanded(
              //   child: Column(
              //     children: [
              //       PopularNowField(
              //         controller: eventType,
              //         hText: "Enter the Event Name",
              //       ),
              //       kNFieldSizedBox,
              //       PopularNowField(
              //         controller: city,
              //         hText: "Enter the City",
              //       ),
              //       kNFieldSizedBox,
              //       ButtonText(
              //         label: 'Search',
              //         onPress: handleSearch,
              //         textColor: Colors.black,
              //       ),
              //     ],
              //   ),
              // ),
              Expanded(

                child: isLoading
                    ? Center(child: CircularProgressIndicator())
                    : ListView.builder(
                  itemCount: response.length,
                  itemBuilder: (context, index) {
                    return Card(
                      child: ListTile(
                        iconColor: Colors.red,
                        leading: Image.asset('image/hotel.jpeg'),
                        title: Text(response[index]['Hname']),
                      ),
                    );
                  },
                ),
              ),

            ],
          ),
        ),
      ),
    );
  }
}

//
//
