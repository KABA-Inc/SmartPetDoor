import {
  Box,
  Button,
  Card,
  Heading,
  Input,
  Stack,
  Text,
  Link as ChackraLink,
} from "@chakra-ui/react";
import { Toaster, toaster } from "../../components/ui/toaster";
import { Link } from "react-router-dom";
import { useState } from "react";
import { register } from "../../api/auth";

const Login = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRegister = async () => {
    setLoading(true);

    try {
      const data = await register(
        firstName,
        lastName,
        email,
        username,
        password
      );
      toaster.create({
        title: "Register successful",
        description: `Welcome, ${data.description}!`,
        type: "success",
        duration: 3000,
      });
      // navigation
    } catch (err: any) {
      toaster.create({
        title: "Register failed",
        description: err.message,
        type: "error",
        duration: 3000,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Toaster />
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minH="100vh"
        bg="brand.50"
        width="100vw"
      >
        <Card.Root
          w="sm"
          shadow="lg"
          borderRadius="xl"
          bg="white"
          border="1px solid"
          borderColor="brand.solid"
        >
          <Card.Header textAlign="center">
            <Heading size="lg" color="brand.solid" fontFamily="heading">
              Smart Pet Door
            </Heading>
          </Card.Header>
          <Card.Body>
            <Stack gap={4}>
              <Input
                placeholder="First Name"
                type="text"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Last Name"
                type="text"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Username"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Input
                placeholder="Confirm Password"
                type="password"
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                borderColor="brand.muted"
                css={{ "--focus-color": "brand.solid" }}
              />
              <Button
                bg="brand.fg"
                color="white"
                _hover={{ bg: "brand.muted", borderColor: "brand.muted" }}
                onClick={handleRegister}
                loading={loading}
              >
                Register
              </Button>
              <Text textAlign="center" fontSize="sm" color="gray.600">
                Already has an account?{" "}
                <ChackraLink
                  asChild
                  fontWeight="bold"
                  color="brand.focusRing"
                  _hover={{ color: "brand.emphasized" }}
                >
                  <Link to="/login">Login</Link>
                </ChackraLink>
              </Text>
            </Stack>
          </Card.Body>
        </Card.Root>
      </Box>
    </>
  );
};

export default Login;
