import React from "react";
import ReactDOM from "react-dom";
import "react-tweet";
import Tweet from 'react-tweet';

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

class MyTweetComponent extends React.Component {
    render() {
        const tweetData = {
            id_str: 'id_str',
            user: {
                name: this.props.data.name,
                screen_name: this.props.data.username
            },
            text: this.props.data.tweets,
            created_at: this.props.data.ymd,
            favorite_count: 'favorite_count',
            retweet_count: 'retweet_count',
            entities: {
                urls: [],
                user_mentions: [],
                hashtags: [],
                symbols: []
            }
        }

        return (
            <Tweet data={tweetData}/>
        )
    }
}

class TweetContainer extends React.Component {
    constructor(props) {
        super(props);
//        this.state = {data: tweetsData}
    }

    render() {
        const listItems = this.props.data.map(
            (d) => <MyTweetComponent data={d}/>
        );
        return (
            <div>{listItems}</div>
        )

    }
}

function renderContainer(data) {
    ReactDOM.render(<TweetContainer data={data}/>,
        document.getElementById("tweets"));
}

//exports.renderContainer = renderContainer;
window.renderContainer = renderContainer;
// ReactDOM.render(<TweetContainer data={tweetsData}/>, document.getElementById("tweets"))
// ReactDOM.render(<App />, document.getElementById("content"));