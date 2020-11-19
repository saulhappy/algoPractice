// const tableColumns = [
//   {
//     name: "id",
//     label: "Id",
//     options: { filter: false, sort: false, display: "exclude" },
//   },
//   {
//     name: "name",
//     label: "Name",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "description",
//     label: "Project Description",
//     options: { filter: true, sort: true },
//   },
//   {
//     name: "type",
//     label: "Type",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "asset",
//     label: "Asset",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "start",
//     label: "Start Date",
//     options: { filter: true, sort: true },
//   },
//   {
//     name: "end",
//     label: "End Date",
//     options: { filter: true, sort: true },
//   },
//   {
//     name: "status",
//     label: "Status",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "asset_condition",
//     label: "Asset Condition",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "reports",
//     label: "Reports",
//     options: { filter: false, sort: false },
//   },
//   {
//     name: "updated_on",
//     label: "Updated",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "created_on",
//     label: "Created",
//     options: {
//       filter: true,
//       sort: true,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
//   {
//     name: "Actions",
//     options: {
//       filter: false,
//       sort: false,
//       empty: true,
//       download: false,
//       print: false,
//       customBodyRender: ["Function: customBodyRender"],
//     },
//   },
// ];

// const customRender = () => {
//   return tableColumns.map((column) => {
//     return column.name;
//   });
// };

// // console.log(customRender());

// console.log(
//   tableColumns.map((column) => {
//     const columnName = column.name;
//     return { columnName };
//   })
// );

// const projectStatus = ''
// const getStatus = projectStatus => {

//   const statusOptions = {
//     'INITIALIZED': {
//       "label" : 'Initialized',
//       "color": "variables.darkestGrey"
//     }, 
//     'ASSIGNED': {
//       "label" : 'Assigned',
//       "color": "variables.darkestGrey"
//     }, 
//     'IN_PROGRESS': {
//       "label" : 'In Progress',
//       "color": "variables.darkestGrey"
//     }, 
//     'READY_FOR_REVIEW': {
//       "label" : 'Ready for Review',
//       "color": "variables.darkestGrey"
//     }, 
//     'PUBLISHED': {
//       "label" : 'Published',
//       "color": "variables.darkestGrey"
//     }, 
  
//   }
  
//   try {
//     return statusOptions[projectStatus];
//    } catch(e) {
//      console.log(e)
//      return {'color': 'unknownColor', 'status': "UNKNOWN"}
//    }
// } 

// console.log(getStatus(projectStatus));

obj = {
  a: 1,
  b: 2, 
  c: 3
}

console.log(obj.a)