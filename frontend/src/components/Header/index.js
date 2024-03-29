import {  NavLink, useNavigate } from "react-router-dom";
import { MainHeader, Navbar, HeaderRight, RegNav } from "./Header.styles";
import LogoLuna from "../../assets/logo.svg"
import {useDispatch, useStore} from "react-redux";
import {useEffect, useState} from "react";
import {clearAuth, setAuth} from "../../features/slice/authSlice";

const Header = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const authData = localStorage.getItem('access');

    useEffect(() => {
      if(authData) setIsLoggedIn(true);
      else setIsLoggedIn(false);
      }, [authData]);

    const handleLogout = () => {

      localStorage.removeItem('access');
      localStorage.removeItem('email');
      dispatch(clearAuth());
      setIsLoggedIn(false)
      navigate("/sign-in")
    };


  return (
    <>
      <MainHeader>
        <img alt="logo" src={LogoLuna} />
        <HeaderRight>
          <Navbar>
            <ul>
              <NavLink to="/">Home</NavLink>
              <NavLink to="/search">Search</NavLink>
              <NavLink to="/user">Profile</NavLink>
            </ul>
          </Navbar>
          <RegNav>
            <button type="button" id="signup" onClick={() => navigate("/sign-up")}>SIGNUP</button>
            {isLoggedIn ? <button type="button" id="logout" onClick={handleLogout}>LOGOUT</button> : <button type="button" id="login" onClick={() => navigate("/sign-in")}>LOGIN</button> }
          </RegNav>
        </HeaderRight>
      </MainHeader>
    </>
  );
};
export default Header;
