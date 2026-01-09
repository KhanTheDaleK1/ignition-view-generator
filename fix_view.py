import json

view_data = {
  "custom": {
    "allSops": [
      { "id": "WI-09-17R03", "title": "WI-09-17R03 Slip Pole Prep", "dept": "Production", "type": "Fitting/Prep", "version": "R03", "url": "/sops/WI-09-17R03 Slip Pole Prep.pdf" },
      { "id": "POLE-LA03-PLANT", "title": "POLE-LA03-PLANT 3 - Pacific Press Brake", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/POLE-LA03-PLANT 3 - Pacific Press Brake.pdf" },
      { "id": "WI-09-12BR03", "title": "WI-09-12BR03 - Cut-Outs", "dept": "Production", "type": "Work Instruction", "version": "R03", "url": "/sops/WI-09-12BR03 - Cut-Outs.pdf" },
      { "id": "WI-09-29R00", "title": "WI-09-29R00 Production Welder Weld Symbols", "dept": "Production", "type": "Welding Procedure", "version": "R00", "url": "/sops/WI-09-29R00 Production Welder Weld Symbols.pdf" },
      { "id": "SOP-GEN", "title": "GMAW 2022 Welding Procedures E80 2G Floor Set with Tables", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/GMAW 2022 Welding Procedures E80 2G Floor Set with Tables.pdf" },
      { "id": "SOP-GEN", "title": "Press Test", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Press Test.pdf" },
      { "id": "SOP-GEN", "title": "SMAW Welding Procedure DS WPS 8018(Tack Weld Proc.)", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/SMAW Welding Procedure DS WPS 8018(Tack Weld Proc.).pdf" },
      { "id": "WI-09-36R00.pdf", "title": "WI-09-36R00", "dept": "Production", "type": "Work Instruction", "version": "R00", "url": "/sops/WI-09-36R00.pdf" },
      { "id": "WI-09-03R06", "title": "WI-09-03R06 Operator Work Instructions for Seam Welder", "dept": "Production", "type": "Welding Procedure", "version": "R06", "url": "/sops/WI-09-03R06 Operator Work Instructions for Seam Welder.pdf" },
      { "id": "WI-09-01AR02", "title": "WI-09-01AR02 Operator Work Instructions for Messer (Plasma)", "dept": "Production", "type": "Plasma Cutting", "version": "R02", "url": "/sops/WI-09-01AR02 Operator Work Instructions for Messer (Plasma).pdf" },
      { "id": "SOP-GEN", "title": "SAW 2021 Welding Procedures A572 Rev0 Floor Set", "dept": "Production", "type": "Welding Procedure", "version": "Rev", "url": "/sops/SAW 2021 Welding Procedures A572 Rev0 Floor Set.pdf" },
      { "id": "WI-10-03R04", "title": "WI-10-03R04 Root Opening Jt Tolerance", "dept": "Quality", "type": "Standards/QA", "version": "R04", "url": "/sops/WI-10-03R04 Root Opening Jt Tolerance.pdf" },
      { "id": "WI-09-01BR05", "title": "WI-09-01BR05 Operator Work Instructions for Kinetic (Plasma)", "dept": "Production", "type": "Plasma Cutting", "version": "R05", "url": "/sops/WI-09-01BR05 Operator Work Instructions for Kinetic (Plasma).pdf" },
      { "id": "WI-09-10AR06", "title": "WI-09-10AR06 Operator Work Instrcutions for the Pacific Press", "dept": "Production", "type": "Press/Forming", "version": "R06", "url": "/sops/WI-09-10AR06 Operator Work Instrcutions for the Pacific Press.pdf" },
      { "id": "SOP-GEN", "title": "ASTM A6A6M-23", "dept": "Quality", "type": "Standards/QA", "version": "1.0", "url": "/sops/ASTM A6A6M-23.pdf" },
      { "id": "SOP-09-02R11", "title": "SOP-09-02R11 tolerances", "dept": "Quality", "type": "Standards/QA", "version": "R11", "url": "/sops/SOP-09-02R11 tolerances.pdf" },
      { "id": "WI-09-10DR01", "title": "WI-09-10DR01 Daily Laser Alignment", "dept": "Quality", "type": "Standards/QA", "version": "R01", "url": "/sops/WI-09-10DR01 Daily Laser Alignment.pdf" },
      { "id": "SOP-GEN", "title": "Small Press WI", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Small Press WI.pdf" },
      { "id": "SOP-09-03R04", "title": "SOP-09-03R04 straightening", "dept": "Production", "type": "Work Instruction", "version": "R04", "url": "/sops/SOP-09-03R04 straightening.pdf" },
      { "id": "WI-09-18R03", "title": "WI-09-18R03 Base Plate Pole Prep", "dept": "Production", "type": "Fitting/Prep", "version": "R03", "url": "/sops/WI-09-18R03 Base Plate Pole Prep.pdf" },
      { "id": "WI-04-14R00", "title": "WI-04-14R00 GM-D1-Gr II to III-CVN-LTD-80 304SS Supplement", "dept": "Production", "type": "Work Instruction", "version": "R00", "url": "/sops/WI-04-14R00 GM-D1-Gr II to III-CVN-LTD-80 304SS Supplement.pdf" },
      { "id": "WI-09-28R01", "title": "WI-09-28R01 Steps to Begin Fit-up", "dept": "Production", "type": "Fitting/Prep", "version": "R01", "url": "/sops/WI-09-28R01 Steps to Begin Fit-up.pdf" },
      { "id": "WI-09-30R00", "title": "WI-09-30R00 Prep Shaft Verification", "dept": "Production", "type": "Fitting/Prep", "version": "R00", "url": "/sops/WI-09-30R00 Prep Shaft Verification.pdf" },
      { "id": "WI-09-10CR03", "title": "WI-09-10CR03 Calibration Instructions for the MINIMAG", "dept": "Quality", "type": "Standards/QA", "version": "R03", "url": "/sops/WI-09-10CR03 Calibration Instructions for the MINIMAG.pdf" },
      { "id": "WI-09-26R02", "title": "WI-09-26R02 - General Weld", "dept": "Production", "type": "Welding Procedure", "version": "R02", "url": "/sops/WI-09-26R02 - General Weld.pdf" },
      { "id": "SOP-GEN", "title": "GMAW 2022 Welding Procedures E80 2G Weathering Full Set with Tables", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/GMAW 2022 Welding Procedures E80 2G Weathering Full Set with Tables.pdf" },
      { "id": "SOP-GEN", "title": "Steel Group Chart - minimum Preheat Table", "dept": "Production", "type": "Work Instruction", "version": "1.0", "url": "/sops/Steel Group Chart - minimum Preheat Table.pdf" },
      { "id": "SOP-GEN", "title": "Seamwelder Parameters", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Seamwelder Parameters.pdf" },
      { "id": "WI-04-13R00", "title": "WI-04-13R00 GM-D1-Gr II to III-CVN-LTD-80 A563 Supplement", "dept": "Production", "type": "Work Instruction", "version": "R00", "url": "/sops/WI-04-13R00 GM-D1-Gr II to III-CVN-LTD-80 A563 Supplement.pdf" },
      { "id": "WI-04-15R00", "title": "WI-04-15R00 GM-D1-Gr II to A871-CVN-LTD-80 304SS Supplement", "dept": "Production", "type": "Work Instruction", "version": "R00", "url": "/sops/WI-04-15R00 GM-D1-Gr II to A871-CVN-LTD-80 304SS Supplement.pdf" },
      { "id": "WI-09-12R03", "title": "WI-09-12R03 SOP PF01 - Basic Pole Fitting", "dept": "Production", "type": "Fitting/Prep", "version": "R03", "url": "/sops/WI-09-12R03 SOP PF01 - Basic Pole Fitting.pdf" },
      { "id": "SOP-GEN", "title": "Kinetic Preventative Maintenance", "dept": "Maintenance", "type": "Maintenance", "version": "1.0", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/Kinetic Preventative Maintenance.pdf" },
      { "id": "SOP-GEN", "title": "Critical Steps for Cutting a Pole on the Kinetic", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/Critical Steps for Cutting a Pole on the Kinetic.pdf" },
      { "id": "SOP-GEN", "title": "Plasma Log", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/Plasma Log.pdf" },
      { "id": "SOP-GEN", "title": "Operator Work Instructions", "dept": "Production", "type": "Work Instruction", "version": "1.0", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/Operator Work Instructions.pdf" },
      { "id": "SOP-GEN", "title": "Plant 3 Kinetic Plasma Master Sheet", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/Plant 3 Kinetic Plasma Master Sheet.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel 260-400amp plasma table", "dept": "Production", "type": "Plasma Cutting", "version": "RAN", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/DISTRAN Steel 260-400amp plasma table.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Material Handler basic JSA", "dept": "Production", "type": "Work Instruction", "version": "RAN", "url": "/sops/Plant 3 Kinetic Plasma (Not Approved)/DISTRAN Steel Material Handler basic JSA.pdf" },
      { "id": "SOP-GEN", "title": "Critical Steps for Cutting a Pole on the Messer", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/Critical Steps for Cutting a Pole on the Messer.pdf" },
      { "id": "SOP-GEN", "title": "Preventative Maintenance for Messer Plasma", "dept": "Maintenance", "type": "Maintenance", "version": "1.0", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/Preventative Maintenance for Messer Plasma.pdf" },
      { "id": "SOP-GEN", "title": "Plant 3 Messer Plasma Master Sheet", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/Plant 3 Messer Plasma Master Sheet.pdf" },
      { "id": "SOP-GEN", "title": "Operator Work Instructions for Messer", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/Operator Work Instructions for Messer.pdf" },
      { "id": "SOP-GEN", "title": "Plasma Log", "dept": "Production", "type": "Plasma Cutting", "version": "1.0", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/Plasma Log.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel 260-400amp plasma table", "dept": "Production", "type": "Plasma Cutting", "version": "RAN", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/DISTRAN Steel 260-400amp plasma table.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Material Handler basic JSA", "dept": "Production", "type": "Work Instruction", "version": "RAN", "url": "/sops/Plant 3 Messer Plasma (Not Approved)/DISTRAN Steel Material Handler basic JSA.pdf" },
      { "id": "SOP-GEN", "title": "PLANT 3 SEAM WELDER MASTER SHEET", "dept": "Production", "type": "Welding Procedure", "version": "R M", "url": "/sops/Plant 3 Seam Welder (Not Approved)/PLANT 3 SEAM WELDER MASTER SHEET.pdf" },
      { "id": "SOP-GEN", "title": "Critical Steps for Seam Welding a Quality Pole", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Critical Steps for Seam Welding a Quality Pole.pdf" },
      { "id": "WI-09-03R06", "title": "WI-09-03R06 Operator Work Instructions for Seam Welder", "dept": "Production", "type": "Welding Procedure", "version": "R06", "url": "/sops/Plant 3 Seam Welder (Not Approved)/WI-09-03R06 Operator Work Instructions for Seam Welder.pdf" },
      { "id": "SOP-GEN", "title": "Copy of Copy of Seamwelder Parameters 2", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Copy of Copy of Seamwelder Parameters 2.pdf" },
      { "id": "SOP-GEN", "title": "Copy of Copy of Seamwelder Parameters 5", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Copy of Copy of Seamwelder Parameters 5.pdf" },
      { "id": "SOP-GEN", "title": "Copy of Copy of Seamwelder Parameters 4", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Copy of Copy of Seamwelder Parameters 4.pdf" },
      { "id": "SOP-GEN", "title": "Seam Welder Log", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Seam Welder Log.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Over head crane JSA", "dept": "Production", "type": "Work Instruction", "version": "RAN", "url": "/sops/Plant 3 Seam Welder (Not Approved)/DISTRAN Steel Over head crane JSA.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Seam Welder JSA", "dept": "Production", "type": "Welding Procedure", "version": "RAN", "url": "/sops/Plant 3 Seam Welder (Not Approved)/DISTRAN Steel Seam Welder JSA.pdf" },
      { "id": "WI-PMR01", "title": "WI-PMR01 Seamwelder Preventative Maintenance", "dept": "Maintenance", "type": "Maintenance", "version": "R01", "url": "/sops/Plant 3 Seam Welder (Not Approved)/WI-PMR01 Seamwelder Preventative Maintenance.pdf" },
      { "id": "SOP-GEN", "title": "Copy of Copy of Seamwelder Parameters 1", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Copy of Copy of Seamwelder Parameters 1.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Material Handler basic JSA", "dept": "Production", "type": "Work Instruction", "version": "RAN", "url": "/sops/Plant 3 Seam Welder (Not Approved)/DISTRAN Steel Material Handler basic JSA.pdf" },
      { "id": "SOP-GEN", "title": "Troubleshooting Seam welder", "dept": "Production", "type": "Welding Procedure", "version": "1.0", "url": "/sops/Plant 3 Seam Welder (Not Approved)/Troubleshooting Seam welder.pdf" },
      { "id": "SOP-GEN", "title": "Camber Check and Flame Straightening", "dept": "Production", "type": "Work Instruction", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Camber Check and Flame Straightening.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Large Press JSA", "dept": "Production", "type": "Press/Forming", "version": "RAN", "url": "/sops/Plant 3 Pacific Press (Not Approved)/DISTRAN Steel Large Press JSA.pdf" },
      { "id": "SOP-GEN", "title": "PLANT 3 PACIFIC PRESS MASTER SHEET", "dept": "Production", "type": "Press/Forming", "version": "RES", "url": "/sops/Plant 3 Pacific Press (Not Approved)/PLANT 3 PACIFIC PRESS MASTER SHEET.pdf" },
      { "id": "SOP-GEN", "title": "Pacific Press Brake Preventative Maintenance", "dept": "Maintenance", "type": "Maintenance", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Pacific Press Brake Preventative Maintenance.pdf" },
      { "id": "SOP-GEN", "title": "Daily Press Log", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Daily Press Log.pdf" },
      { "id": "SOP-GEN", "title": "Pacific Press Brake Die Spacing Change", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Pacific Press Brake Die Spacing Change.pdf" },
      { "id": "SOP-GEN", "title": "Pacific Press Brake Work Instructions", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Pacific Press Brake Work Instructions.pdf" },
      { "id": "SOP-GEN", "title": "Critical Steps for Pressing a Quality Pole", "dept": "Production", "type": "Press/Forming", "version": "1.0", "url": "/sops/Plant 3 Pacific Press (Not Approved)/Critical Steps for Pressing a Quality Pole.pdf" },
      { "id": "SOP-GEN", "title": "DISTRAN Steel Material Handler basic JSA", "dept": "Production", "type": "Work Instruction", "version": "RAN", "url": "/sops/Plant 3 Pacific Press (Not Approved)/DISTRAN Steel Material Handler basic JSA.pdf" }
    ]
  },
  "params": {},
  "props": {
    "defaultSize": { "height": 800, "width": 1280 }
  },
  "root": {
    "meta": { "name": "root" },
    "props": {
      "direction": "column",
      "style": { "backgroundColor": "#121212", "height": "100%", "overflow": "hidden" }
    },
    "children": [
      {
        "meta": { "name": "Header" },
        "position": { "basis": "auto", "shrink": 0 },
        "props": {
          "style": { "alignItems": "center", "backgroundColor": "#1F1F1F", "borderBottom": "4px solid #FF6600", "display": "flex", "justifyContent": "space-between", "padding": "10px 20px", "flexWrap": "wrap", "gap": "10px", "minHeight": "60px", "boxShadow": "0 2px 4px rgba(0,0,0,0.3)" }
        },
        "children": [
          {
            "meta": { "name": "Title" },
            "props": { "style": { "color": "#FFFFFF", "fontSize": "clamp(1.2rem, 3vw, 1.5rem)", "fontWeight": "bold" }, "text": "KNOWLEDGEBASE PORTAL" },
            "type": "ia.display.label"
          },
          {
            "meta": { "name": "SearchInput" },
            "position": { "basis": "250px", "grow": 1 },
            "propConfig": {
              "props.value": {
                "binding": { "config": { "bidirectional": True, "path": "view.custom.searchText" }, "type": "property" }
              }
            },
            "props": { "placeholder": "Search SOPs (Content or Title)...", "style": { "backgroundColor": "#2D2D2D", "color": "#FFF", "borderRadius": "4px", "border": "1px solid #FF6600" } },
            "type": "ia.input.text-field"
          }
        ],
        "type": "ia.container.flex"
      },
      {
        "meta": { "name": "ContentBody" },
        "position": { "grow": 1 },
        "props": { "direction": "row", "wrap": "wrap", "style": { "overflow": "hidden", "width": "100%", "height": "100%" } },
        "children": [
          {
            "meta": { "name": "Sidebar" },
            "position": { "basis": "300px", "grow": 1, "shrink": 0 },
            "props": { "direction": "column", "style": { "backgroundColor": "#1E1E1E", "borderRight": "2px solid #333", "padding": "20px", "gap": "20px", "overflowY": "auto", "minWidth": "250px" } },
            "children": [
              { "props": { "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold", "textTransform": "uppercase" }, "text": "Filters" }, "type": "ia.display.label" },
              { "props": { "style": { "color": "#E0E0E0", "fontSize": "12px", "fontWeight": "bold", "marginTop": "10px" }, "text": "DEPARTMENT" }, "type": "ia.display.label" },
              {
                "meta": { "name": "DeptFilter" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedDept" }, "type": "property" } } },
                "props": {
                  "options": [
                    { "label": "All Departments", "value": "All" },
                    { "label": "Production", "value": "Production" },
                    { "label": "Quality", "value": "Quality" },
                    { "label": "Maintenance", "value": "Maintenance" }
                  ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              { "props": { "style": { "color": "#E0E0E0", "fontSize": "12px", "fontWeight": "bold", "marginTop": "10px" }, "text": "SOP TYPE" }, "type": "ia.display.label" },
              {
                "meta": { "name": "TypeFilter" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedType" }, "type": "property" } } },
                "props": {
                  "options": [
                    { "label": "All Types", "value": "All" },
                    { "label": "Work Instruction", "value": "Work Instruction" },
                    { "label": "Welding Procedure", "value": "Welding Procedure" },
                    { "label": "Plasma Cutting", "value": "Plasma Cutting" },
                    { "label": "Press/Forming", "value": "Press/Forming" },
                    { "label": "Fitting/Prep", "value": "Fitting/Prep" },
                    { "label": "Standards/QA", "value": "Standards/QA" },
                    { "label": "Maintenance", "value": "Maintenance" }
                  ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              { "props": { "style": { "borderTop": "1px solid #444", "marginTop": "20px" } }, "type": "ia.display.label" },
              { "props": { "style": { "color": "#FF6600", "fontSize": "14px", "fontWeight": "bold", "textTransform": "uppercase" }, "text": "Maps" }, "type": "ia.display.label" },
              {
                "meta": { "name": "SiteDropdown" },
                "propConfig": { "props.value": { "binding": { "config": { "bidirectional": True, "path": "view.custom.selectedMapUrl" }, "type": "property" } } },
                "props": {
                  "options": [
                    { "label": "Pineville Full Site", "value": "https://us.hamina.com/share/9914cd75-d81e-4d85-af1f-b198cd2d6119" },
                    { "label": "Pineville Plant 1", "value": "https://us.hamina.com/share/d9f7e46a-9a2b-4a27-94bf-a94081f2934d" },
                    { "label": "Pineville Plant 2", "value": "https://us.hamina.com/share/3b3a0e9f-5083-484c-8500-5be36c975b13" },
                    { "label": "Pineville Plant 3", "value": "https://us.hamina.com/share/ab7a57a0-aa95-40f8-a514-b8cf13b0aad2" },
                    { "label": "Pineville Plant 4", "value": "https://us.hamina.com/share/5e892eee-15cc-4887-b45b-bd642b431aa6" },
                    { "label": "Eunice", "value": "https://us.hamina.com/share/2b3b6251-51e8-4c7e-a1e6-7da2d7d9ac94" }
                  ],
                  "style": { "backgroundColor": "#2D2D2D", "color": "#FFF" }
                },
                "type": "ia.input.dropdown"
              },
              {
                "events": { "component": { "onActionPerformed": { "config": { "script": "\tsystem.perspective.navigate(url=self.view.custom.selectedMapUrl, newTab=True)" }, "scope": "G", "type": "script" } } },
                "props": { "style": { "backgroundColor": "#FF6600", "color": "#FFF", "fontWeight": "bold", "marginTop": "10px" }, "text": "OPEN INTERACTIVE MAP" },
                "type": "ia.input.button"
              }
            ],
            "type": "ia.container.flex"
          },
          {
            "meta": { "name": "MainResults" },
            "position": { "basis": "600px", "grow": 999, "shrink": 1 },
            "props": { "direction": "column", "style": { "backgroundColor": "#121212", "padding": "20px", "overflowY": "auto", "height": "100%" } },
            "children": [
              {
                "meta": { "name": "SOP_Repeater" },
                "propConfig": {
                  "props.instances": {
                    "binding": {
                      "config": { "path": "view.custom.allSops" },
                      "transforms": [
                        {
                          "code": "\tdept = self.view.custom.selectedDept\n\ttype_ = self.view.custom.selectedType\n\tsearch = self.view.custom.searchText.lower()\n\tfiltered = []\n\tfor sop in value:\n\t\tif (dept == 'All' or sop['dept'] == dept) and (type_ == 'All' or sop['type'] == type_) and (search == '' or search in sop['title'].lower() or search in sop.get('keywords', '').lower()):\n\t\t\tfiltered.append(sop)\n\treturn filtered",
                          "type": "script"
                        }
                      ],
                      "type": "property"
                    }
                  }
                },
                "props": { "direction": "row", "path": "Page/Knowledgebase/SOP_Card", "style": { "display": "flex", "flexWrap": "wrap", "gap": "20px", "justifyContent": "center", "alignContent": "flex-start" } },
                "type": "ia.display.flex-repeater"
              }
            ],
            "type": "ia.container.flex"
          }
        ],
        "type": "ia.container.flex"
      }
    ],
    "type": "ia.container.flex"
  }
}

with open('/mnt/projects/7. Ignition/data/projects/OT_Sandbox/com.inductiveautomation.perspective/views/Page/Knowledgebase/view.json', 'w') as f:
    json.dump(view_data, f, indent=2)
print("Successfully generated view.json")
