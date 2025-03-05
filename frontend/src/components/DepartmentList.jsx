import React, { useEffect, useState } from "react";
import API from "../api"; // Import your Axios instance

const DepartmentList = () => {
  const [departments, setDepartments] = useState([]);

  // Fetch departments when the component mounts
  useEffect(() => {
    API.get("department/")
      .then((response) => {
        setDepartments(response.data);
      })
      .catch((error) => {
        console.error("Error fetching departments:", error);
      });
  }, []);

  return (
    <div>
      <h2>Departments</h2>
      <ul>
        {departments.map((dept) => (
          <li key={dept.id}>
            <strong>{dept.department_name}</strong><p>{dept.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DepartmentList;
