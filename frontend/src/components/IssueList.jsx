// import React, { useEffect, useState } from "react";
// import API from "../api";  // Adjust the path if necessary

// const IssueList = () => {
//   const [issues, setIssues] = useState([]);

//   // Fetch issues when the component mounts
//   useEffect(() => {
//     API.get("issues/")
//       .then((response) => {
//         setIssues(response.data);
//       })
//       .catch((error) => {
//         console.error("Error fetching issues:", error);
//       });
//   }, []);

//   return (
//     <div>
//       <h2>Issues</h2>
//       <ul>
//         {issues.map((issue) => (
//           <li key={issue.id}>
//             <strong>{issue.title}   {issue.status} ++++ {issue.course_unit} </strong> - {issue.description}  {issue.created_at}
//             {issue.department && ` (Dept: ${issue.department.name})`}
            
//           </li>
          
//         ))}
//       </ul>
    
//     </div>
//   );
// };

// export default IssueList;

import React, { useEffect, useState } from "react";
import API from "../api"; // Adjust the path if necessary
import './IssueList.css';
const IssueList = () => {
  const [issues, setIssues] = useState([]);

  // Fetch issues when the component mounts
  useEffect(() => {
    API.get("issues/")  // This is where the request is made
      .then((response) => {
        setIssues(response.data);  // Update state with the fetched issues
      })
      .catch((error) => {
        console.error("Error fetching issues:", error);
      });
  }, []); // Empty dependency array means it runs once when the component mounts

  return (
    <div>
      <h2>Issues</h2>
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Status</th>
            <th>Course Unit</th>
            <th>Description</th>
            <th>Created At</th>
            <th>Department</th>
          </tr>
        </thead>
        <tbody>
          {issues.map((issue) => (
            <tr key={issue.id}>
              <td>{issue.title}</td>
              <td>{issue.status}</td>
              <td>{issue.course_unit}</td>
              <td>{issue.description}</td>
              <td>{issue.created_at}</td>
              <td>{issue.department ? issue.department.name : 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default IssueList;

