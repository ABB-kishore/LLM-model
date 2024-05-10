#prompts

dictionary = {
    "Table1": """Could you please provide a breakdown of the IO counts for all areas and systems as specified in the RFQ document also add one row "total" in the last to give total count of all areas? Please format the response in JSON format with the following structure
      {
  'areas': {
    'area1': {
      'systems': {
        'DCS': {
          'analog_inputs': 100,
          'analog_outputs': 50,
          'digital_inputs': 200,
          'digital_outputs': None
        },
        'FGS': {
          'analog_inputs': 50,
          'digital_inputs': 100
        },
        'ESD': {
          'digital_inputs': None,
          'digital_outputs': 25
        }
      }
    },
    'area2': {
      'systems': {
        'DCS': {
          'analog_inputs': 75,
          'analog_outputs': 40,
          'digital_inputs': 150,
          'digital_outputs': 100
        },
        'FGS': {
          'analog_inputs': 40,
          'digital_inputs': 75
        },
        'ESD': {
          'digital_inputs': 40,
          'digital_outputs': None
        }
      }
    }
  }
}
If  area or system is not specified in the RFQ document, please omit the corresponding entry from the JSON response.""",

    "scope": """What is the overall ICSS vendor scope?\n Give the answer in short and crisp points.
            Assume as if you are the ABB vendor and give the answer.The first line should be in a tone as if you are the ABB vendor. 
           For Example:Our scope shall be to supply  the Integrated Control & Safety System (ICSS). Our solution encompasses as per below
           - Safety Instrumented System (SIS) 
           - Process Shutdown System (PSD) """,

    "System": "What are the sytems provided in document. give answers in short and crisp points",

    "controllers": "What are the controllers that are redundant. give answers in short and crisp points",

    "Third": """Is ICSS third party Integration is available in the doucument? If yes then check for Kepware software mentioned. If mentioned then print 'kepware software' else print below in triple back ticks nothing else.
           ```
           PLC Connect

           Redundant Communication Module
           ------------------------------ 
        −	Modbus TCP/IP : CI867 
        −	Serial (RS232/485) : CI853
        −	IEC61850 : CI868 
        −	Profibus DP : CI854A 
        −	Foundation Fieldbus HSE :CI860 
        −	PROFINET(SELECT IO) :CI871  
        ```
          
          """,

    "Red": """What are the Redundant /Non-Redundant Networks availble in document. Give answer in short and crisp points. Answer format must be in below format written inside tripple back ticks.
           Also make sure keep points mentioned in below example as default points and start adding new points from below next points.
           
           ```
        Redundant Network offered for 
        -----------------------------
        −	Client/Server HMI Network 
        −	Control Network 
        −	Plant Information Network 
           
        Non-Redundant Network offered for 
        ---------------------------------
        −
           ```
           """,

    "serve": """What are the redundant servers mentioned in the document. Give answer in short and crisp points. Answer format must be in below format written inside tripple back ticks.
           Also Does DCS communicate to Third party Integration? If yes then check via OPC server. If mentioned then add new point 'OPC server' in 'Virtualised server are offered for'.
           Also make sure keep points mentioned in below example as default points and start adding new points from below next points.

           ```
            Virtualised server are offered for 
            ----------------------------------
            −	800xA System Servers (Aspect/ Connectivity/Domain)
            -

            Physical dedicated server are offered for 
            -----------------------------------------
            −	800xA History Server  
           
            ```

           """,

    "Spare": "What percentage of Installed I/O Spares are included in the document? Provide a one-word answer in percentage.",

    "space": "What percentage of Spare Space in Indoor Cabinets is considered in the document? Provide a one-word answer in percentage",

    "safe": "Is it Intrinsic safe signals? Give answer as 'YES' or 'NO'",

    "Non": "Does Digital output Signal of DCS is provided with interposing relay? If 'yes' then then write 'yes' and provide details like voltage and current rating of interposing relay DO nothing else. If 'no' then print 'NO' nothing else. Give answer in short and crisp points.",

    "SIL": "Does the document specifically address the use of interposing relays for SIL applications? Please respond with either 'Yes' or 'No'",

    "Redun": """What are the items which are redundant as per the document? answer must be short and crisp points nothing else.""",

    "HART": " Does Analog input and Analog output signals are provided for HART pass through I/O modules? If 'yes' then then write 'yes, AI/AO'. If 'no' then print 'NO' nothing else.",

    "Graphics": "What are the total number Graphics Count? give one word answer in number format only nothing else.",

    "histo": "Quantity of redundant or non-redundant historian or history logs. Give one word answer in number format only, if not mentioned the return 'None'.",

    "Repo1": "What is the Quantity of Simple reports (Status & Maintenance)? Give one word answer in number format only, if not mentioned the return 'None'.",

    "Repo2": "What is the Quantity of Complex reports (Production)? Give one word answer in number format only, if not mentioned the return 'None'.",

    "nonred": "What are the Non-Redundant Networks availble in document. Give servers name answer in short and crisp points nothing else. Does the RFQ provide the details of Field Device(or Device) Diagnostic Management as DCS vendor scope? if yes then add 'Field Information Manager (FIM) Server' in the point. Also check for cyber security server mentioned in the document. If mentioned then add 'Cyber Security Server' in the point. "

}
