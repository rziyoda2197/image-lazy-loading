import React from 'react';

class LazyImage extends React.Component {
    constructor(props) {
        super(props);
        this.imageRef = React.createRef();
    }

    componentDidMount() {
        this.imageRef.current.addEventListener('load', () => {
            this.imageRef.current.classList.add('loaded');
        });
    }

    render() {
        return (
            <div className="lazy-image">
                <img
                    ref={this.imageRef}
                    src={this.props.placeholder}
                    data-src={this.props.src}
                    alt={this.props.alt}
                    onLoad={() => {
                        this.imageRef.current.classList.add('loaded');
                    }}
                />
            </div>
        );
    }
}

class App extends React.Component {
    render() {
        return (
            <div>
                <LazyImage
                    placeholder="https://via.placeholder.com/300"
                    src="https://picsum.photos/300/300"
                    alt="Lazy loaded image"
                />
            </div>
        );
    }
}

export default App;
```

```css
.lazy-image img {
    transition: opacity 0.5s;
    opacity: 0;
}

.lazy-image img.loaded {
    opacity: 1;
}
