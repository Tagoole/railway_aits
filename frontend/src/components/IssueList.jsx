import React, { useEffect, useState } from "react";
import API from "../api";  // Adjust the path if necessary

const IssueList = () => {
  const [issues, setIssues] = useState([]);

  // Fetch issues when the component mounts
  useEffect(() => {
    API.get("issues/")
      .then((response) => {
        setIssues(response.data);
      })
      .catch((error) => {
        console.error("Error fetching issues:", error);
      });
  }, []);

  return (
    <div>
      <h2>Issues</h2>
      <ul>
        {issues.map((issue) => (
          <li key={issue.id}>
            <strong>{issue.title}   {issue.status} ++++ {issue.course_unit} </strong> - {issue.description}  {issue.created_at}
            {issue.department && ` (Dept: ${issue.department.name})`}
            
          </li>
        ))}
      </ul>
    </div>
  );
};

export default IssueList;
