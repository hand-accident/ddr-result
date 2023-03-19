<script>
    let className;
    export { className as class };
    export let href;
</script>

<a {href} class="c {className}">
    <slot />
</a>

<style lang="postcss" module>
    .c {
        @apply link;
    }
</style>
