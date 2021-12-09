# Writing CSS

In some cases it is necessary to write your own custom stylesheets,
when bootstrap don't provide the required predefined styles.
These stylesheets are typically related to a specific component, like `Chip.less` is related to `Chip.js`.

When creating a stylesheet to a specific component should you give it identical names, suffixed with `.less`,
such that we can easily identify the component the styles are related to. If your styles don't naturally relate to a component, it might be some general/universal styles,
try and find a parent component where it could be natural to place the styles.

> Styles defined for a component should always come from the component's own stylesheet or a parent component, never a child component.
> This is to match the cascading nature of CSS.

When writing custom styles use the [Block Element Modifier (BEM) methodology](https://css-tricks.com/bem-101/).
This is a methodology designed to be easy to read and maintain, and it also matches [nav's](https://navikt.github.io/nav-frontend-moduler/#/) writing style.

#### Simple example

Given our component `Chip.js` bellow. We need some styling to make this component presentable,
and both the container and children need their own styles. For this simple example could we of course instead just set a class on the container,
and use simple CSS nesting, but for the sake of this example will we use _BEM_.

```jsx
// Chip.js

// Container has the general classname "chip"
const Chip = ({ label }) => (
  <div className="chip">
    // Each children, needing styles, is prefixed with "chip" and the delimiter "__"
    <em className="chip__label">{label}</div>
    <button className="chip__button">X</button>
  </div>
);
```

Then in the stylesheets can we define the classes as usual. Remember to not nest `chip__label` and `chip__button` inside `chip`.
i.e. don't do this `.chip .chip__label`. The point of BEM is to keep a more flat structure, with minimal side-effects from nesting.

```less
.chip {
  // Some styles to the container
}

.chip__label {
  // Some styling
}

.chip__button {
  // Some styling
}

// This is equivalent in LESS to

.chip {
  // Some styles to the container

  &__label {
    // Some styling
  }

  &__button {
    // Some styling
  }
}
```

Now say we wan't to change a chips color. This is the use-case for the **M**odifier in BE**M**.

```jsx
// Chip.js

// The chip is now colored
// The "--" tells us that it is a modifier to chip
const Chip = ({ label }) => (
  <div className="chip chip--organge">
    // Each children, needing styles, is prefixed with "chip" and the delimiter "__"
    <em className="chip__label">{label}</div>
    <button className="chip__button">X</button>
  </div>
);
```
