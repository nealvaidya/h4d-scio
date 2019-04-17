import React from "react";
import ReactDOM from "react-dom";
import TweetContainer from "./mytweetcomponent";
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Paper from '@material-ui/core/Paper'
import InputBase from '@material-ui/core/InputBase'
import Eye from 'mdi-material-ui'
import IconButton from '@material-ui/core/IconButton'
import { Icon } from "@material-ui/core";

const data = {
    description: "",
    followers: 0,
    location: "Read my blog",
    name: "Rami",
    tweets: "28 killed",
    username: "RamiAlLolah",
    ymd: "2016-02-16"
}

const tweetsData = [data]

function renderContainer(data) {
    ReactDOM.render(<TweetContainer data={data}/>,
        document.getElementById("tweets"));
}

function SearchBar(props) {
    return (
        <Paper>
            <InputBase placeholder="Search"/>
            <IconButton>
                <Eye />
            </IconButton>
        </Paper>
    )
}

ReactDOM.render(<SearchBar />,
    document.getElementById("similar-words"))

//exports.renderContainer = renderContainer;
window.renderContainer = renderContainer;
// ReactDOM.render(<TweetContainer data={tweetsData}/>, document.getElementById("tweets"))
// ReactDOM.render(<App />, document.getElementById("content"));