// import React, { useEffect, useState } from "react";
// import API from "../api"; // Import your Axios instance

// const DepartmentList = () => {
//   const [departments, setDepartments] = useState([]);

//   // Fetch departments when the component mounts
//   useEffect(() => {
//     API.get("department/")
//       .then((response) => {
//         setDepartments(response.data);
//       })
//       .catch((error) => {
//         console.error("Error fetching departments:", error);
//       });
//   }, []);

//   return (
//     <div>
//       <h2>Departments</h2>
//       <ul>
//         {departments.map((dept) => (
//           <li key={dept.id}>
//             <strong>{dept.department_name}</strong>
//           </li>
//         ))}
//       </ul>
//     </div>
//   );
// };

// export default DepartmentList;

import React, { useEffect, useState } from "react";
import API from "../api"; // Import the Axios instance

const DepartmentList = () => {
  const [departments, setDepartments] = useState([]);

  // Fetch departments when the component mounts
  useEffect(() => {
    API.get("department/")  // This is where the request is made
      .then((response) => {
        setDepartments(response.data);  // Update state with the fetched departments
      })
      .catch((error) => {
        console.error("Error fetching departments:", error);
      });
  }, []); // Empty dependency array means it runs once when the component mounts

  return (
    <div>
      <h2>Departments</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse' }}>
        <thead>
          <tr>
            <th style={{ padding: '8px', textAlign: 'left', border: '1px solid #ddd', backgroundColor: '#f4f4f4' }}>Department Name</th>
            <th style={{ padding: '8px', textAlign: 'left', border: '1px solid #ddd', backgroundColor: '#f4f4f4' }}>Description</th>
          </tr>
        </thead>
        <tbody>
          {departments.map((dept) => (
            <tr key={dept.id}>
              <td style={{ padding: '8px', textAlign: 'left', border: '1px solid #ddd' }}>{dept.department_name}</td>
              <td style={{ padding: '8px', textAlign: 'left', border: '1px solid #ddd' }}>{dept.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DepartmentList;
