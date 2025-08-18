const API_URL = import.meta.env.VITE_API_URL;

export const login = async (username: string, password: string) => {
  const userData = {
    username: username,
    password: password,
  };
  const response = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    throw new Error("Error: " + response);
  }

  const data = await response.json();
  return data;
};

export const register = async (
  firstName: string,
  lastName: string,
  email: string,
  username: string,
  password: string
) => {
  const userData = {
    first_name: firstName,
    last_name: lastName,
    email: email,
    username: username,
    password: password,
  };
  console.log(userData);

  const response = await fetch(`${API_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });

  if (!response.ok) {
    throw new Error("Error: " + response);
  }

  const data = await response.json();
  return data;
};
